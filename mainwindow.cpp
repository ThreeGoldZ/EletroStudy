#include "mainwindow.h"
#include "ui_mainwindow.h"
#include <QTextStream>

static TIMER t;
#define DAC_VSCALAR 32767		// Binary-to-volts scalar for Sensoray 826 analog output
#define SAMPLE_RATE (10000)
#define pi 3.14159
#define cMax 2.5
#define _USE_MATH_DEFINES
#define NUMBEROFDATA 40000
static char outputfilepath[200];


static int ao1 = 0;
static int ao2 = 1;
static int ao3 = 2;
static int ao4 = 3;
static int ao5 = 4;
static int ao6 = 5;
static int ao7 = 6;
static int ao8 = 7;

static int counter = -1;
static int arr[] = { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9,10,11 };


static int counterj = 0;
static int lVib;

static uint board = 0; // identifier for Sensoray 826 board
static int errcode = S826_ERR_OK; // error code for Sensoray 826 board

static int dirNum = 0; // 0 = right, 1 = left

static char key; // last key that was pressed
static volatile bool exitKey = false; // Boolean looking for exit key

static bool playVib = false;

static float textVib[5000];
static float textVib1[5000];
static float textVib2[5000];
static bool textOne = true;

static int pWidth = 2600; // pulse width (ms)
static float pDelay = 0.125; // delay of sequential pulses (percentage of pWidth)


//experiment variables
QList<int> tester_choice;
QList<int> tester_reaction;
int last_choice = 0;
int perception_threshold = 0;
int discomfort_threshold = 0;
bool perception_checking = false;
bool perception_checkpoint_found = false;
bool perception_threshold_found = false;
bool discomfort_checking = false;
bool discomfort_checkpoint_found = false;
bool discomfort_threshold_found = false;
int tester_file_number = 1;
QTextStream info(stdout);
int trial_counter = 1;

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// ERROR HANDLING
// These examples employ very simple error handling: if an error is detected, the example functions will immediately return an error code.
// This behavior may not be suitable for some real-world applications but it makes the code easier to read and understand. In a real
// application, it's likely that additional actions would need to be performed. The examples use the following X826 macro to handle API
// function errors; it calls an API function and stores the returned value in errcode, then returns immediately if an error was detected.

#define X826(FUNC)   if ((errcode = FUNC) != S826_ERR_OK) { printf("\nERROR: %d\n", errcode); return errcode;}

///////// FUNCTION PROTOTYPES ///////////
void keyInput(); // handles input from keyboard to play actuators and change directions
void hapticsLoop(); // calculates and outputs signals to voice coils
void hapticsTest();
char * runFile();

//vector<int> findLocation(string sample, char findIt);

// Timer function

static double StartTime = 0;
static double CurrentTime = 0;

static float aod1[NUMBEROFDATA];
static float aod2[NUMBEROFDATA];
static float aod3[NUMBEROFDATA];
static float aod4[NUMBEROFDATA];
static float aod5[NUMBEROFDATA];
static float aod6[NUMBEROFDATA];
static float aod7[NUMBEROFDATA];
static float aod8[NUMBEROFDATA];


static double outVC1 = 0.0;
static double outVC2 = 0.0;
static double outVC3 = 0.0;
static double outVC4 = 0.0;
static double outVC5 = 0.0;
static double outVC6 = 0.0;
static double outVC7 = 0.0;
static double outVC8 = 0.0;

//Result recording initializations
FILE *resultsFile;
QString participant_id;
QString moisture_percent;
QString partnumber;
bool first_time = true;


MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    ui->label_5->setText(QString::number(tester_file_number));
    strcpy(outputfilepath, "C:\\Users\\hmcul\\Desktop\\StudyUI_Results\\3.txt");
}

MainWindow::~MainWindow()
{
    delete ui;
}

static int readData(char* filepath){


    FILE *fptr;

    char *data;
    data = (char *)malloc(128 * sizeof(char));

    fptr = fopen(filepath, "r");

    if (fptr == NULL) {
        printf("Error! opening file");
        getchar();
        // Program exits if the file pointer returns NULL.
        exit(1);
    }

    int i = 0;
    while (1) {
        int r = fscanf(fptr, "%f %f %f %f %f %f %f %f ", &aod1[i], &aod2[i], &aod3[i],&aod4[i], &aod5[i], &aod6[i],&aod7[i],&aod8[i]);
        if (r == EOF)
            break;
        i++;
    }
    fclose(fptr);
    return i;
}

void MainWindow::on_play_clicked()
{
    ui->label_5->setText(QString::number(tester_file_number));
    ui->feel_good->setDisabled(false);
    ui->feel_strong->setDisabled(false);
    ui->feel_nothing->setDisabled(false);
    ui->feel_something->setDisabled(false);
    ui->increase_five->setDisabled(true);
    ui->decrease_five->setDisabled(true);
    ui->increase_one->setDisabled(true);
    ui->decrease_one->setDisabled(true);



    tester_choice.append(tester_file_number);
    //tester_file_number +=1;
    QString strf = QString::number(tester_file_number) + ".txt";
    //QString strf= "1.txt";

    //Get the names of the files
    QByteArray ba = strf.toLocal8Bit();
    const char *signalname = ba.data();
    char filepath[200];
    //strcpy( filepath, "D:\\DesktopFile\\xinzhu\\Study\\DataRecordings_Hejia\\" );
    //strcpy( filepath, "D:\\Frontier2021Study\\dataRecording\\Processed Signals\\Processed Signals\\processed_data_98\\processed_data_98\\" );
    strcpy( filepath, "D:\\DesktopFile\\xinzhu\\study_data\\");
    strcat( filepath, signalname );
   // filepath[] ="D:\\DesktopFile\\xinzhu\\Study\\DataRecordings_Hejia\\")+signalname;
    // for (int i=0;i<12;i++)



    //declear variables
    counterj=0;
    S826_SystemOpen();
    S826_DacRangeWrite(board, 0, S826_DAC_SPAN_5_5, 0) ;
    S826_DacRangeWrite(board, 1, S826_DAC_SPAN_5_5, 0) ;
    S826_DacRangeWrite(board, 2, S826_DAC_SPAN_5_5, 0) ;
    S826_DacRangeWrite(board, 3, S826_DAC_SPAN_5_5, 0) ;
    S826_DacRangeWrite(board, 4, S826_DAC_SPAN_5_5, 0) ;
    S826_DacRangeWrite(board, 5, S826_DAC_SPAN_5_5, 0) ;
    S826_DacRangeWrite(board, 6, S826_DAC_SPAN_5_5, 0) ;
    S826_DacRangeWrite(board, 7, S826_DAC_SPAN_5_5, 0) ;

    //int tStep =  / 4; // 1/4 pulse width of the actuator indent (ms)
    float deltaT = 0.0;
    int iLoop;
    int datacount = readData(filepath);


    for (iLoop = 0; iLoop < datacount; iLoop++)
    {
        StartTime = t.seconds(); // start time of each time through loop
        deltaT = 0.0;
        // Wait function for 1 ms. Haptic loop outputs new values at 1000 Hz
        while (deltaT <= (double)1/SAMPLE_RATE)
        {
            CurrentTime = t.seconds();
            deltaT = CurrentTime - StartTime;
        }

        if ( counterj < datacount)
        {
               outVC1 = cMax *aod1[counterj]*5;
               outVC2 = cMax *aod2[counterj]*5;
               outVC3 = cMax *aod3[counterj]*5;
               outVC4 = cMax *aod4[counterj]*5;
               outVC5 = cMax *aod5[counterj]*5;
               outVC6 = cMax *aod6[counterj]*5;
               outVC7 = cMax *aod7[counterj]*5;
               outVC8 = cMax *aod8[counterj]*5;
               //printf("%d\n",counterj);
               //printf("%f\n", outVC1);
               counterj++;
        }

         S826_DacDataWrite(board, ao1, (uint)(DAC_VSCALAR + outVC1 / 5.0*DAC_VSCALAR), 0);
         S826_DacDataWrite(board, ao2, (uint)(DAC_VSCALAR + outVC2 / 5.0*DAC_VSCALAR), 0);
         S826_DacDataWrite(board, ao3, (uint)(DAC_VSCALAR + outVC3 / 5.0*DAC_VSCALAR), 0);
         S826_DacDataWrite(board, ao4, (uint)(DAC_VSCALAR + outVC4 / 5.0*DAC_VSCALAR), 0);
         S826_DacDataWrite(board, ao5, (uint)(DAC_VSCALAR + outVC5 / 5.0*DAC_VSCALAR), 0);
         S826_DacDataWrite(board, ao6, (uint)(DAC_VSCALAR + outVC6 / 5.0*DAC_VSCALAR), 0);
         S826_DacDataWrite(board, ao7, (uint)(DAC_VSCALAR + outVC7 / 5.0*DAC_VSCALAR), 0);
         S826_DacDataWrite(board, ao8, (uint)(DAC_VSCALAR + outVC8 / 5.0*DAC_VSCALAR), 0);

    //END FOR ILOOP <I
    }
    iLoop = 0; // zero counter

    S826_DacDataWrite(board, ao1, (uint)(DAC_VSCALAR), 0);
    S826_DacDataWrite(board, ao2, (uint)(DAC_VSCALAR), 0);
    S826_DacDataWrite(board, ao3, (uint)(DAC_VSCALAR), 0);
    S826_DacDataWrite(board, ao4, (uint)(DAC_VSCALAR), 0);
    S826_DacDataWrite(board, ao5, (uint)(DAC_VSCALAR), 0);
    S826_DacDataWrite(board, ao6, (uint)(DAC_VSCALAR), 0);
    S826_DacDataWrite(board, ao7, (uint)(DAC_VSCALAR), 0);
    S826_DacDataWrite(board, ao8, (uint)(DAC_VSCALAR), 0);

    S826_SystemClose(); // close Sensoray 826 board
   // s1=new StudyMode();
    //s1->show();

}

void MainWindow::on_increase_five_clicked()
{
    //change  file number
    tester_file_number += 5;

    ui->label_5->setText(QString::number(tester_file_number));

    //record


}

void MainWindow::on_decrease_five_clicked()
{
    //change  file number
    tester_file_number -= 5;

    ui->label_5->setText(QString::number(tester_file_number));


}

void MainWindow::on_increase_one_clicked()
{
    //change  file number
    tester_file_number += 1;


    ui->label_5->setText(QString::number(tester_file_number));

    //record
    //tester_choice.append(tester_file_number);

}

void MainWindow::on_decrease_one_clicked()
{
    //change  file number
    tester_file_number -= 1;


    ui->label_5->setText(QString::number(tester_file_number));

    //record
    //tester_choice.append(tester_file_number);

}

void MainWindow::on_feel_nothing_clicked()
{
    //File initializer for recording the results
    resultsFile = fopen(outputfilepath, "a");

    if (resultsFile == NULL) {
        printf("Error! opening file");
        getchar();
        // Program exits if the file pointer returns NULL.
        exit(1);
    }
    participant_id = ui->participant_id->text();
    //std::string parti = participant_id.toUtf8().constData();
    moisture_percent =ui->moisture_percent->text();
    partnumber= ui->part_no->currentText();
    //print participant number
    fprintf(resultsFile, "%s, ", participant_id.toStdString().c_str());
    //print moisture level
    fprintf(resultsFile, "%s, ", moisture_percent.toStdString().c_str());
    //print partnumber
    fprintf(resultsFile, "%s, ", partnumber.toStdString().c_str());
    //print signal number
    fprintf(resultsFile, "%d, ", tester_file_number);
    //print feeling number
    fprintf(resultsFile, "1\n");
    tester_reaction.append(1);
    ui->feel_good->setDisabled(true);
    ui->feel_strong->setDisabled(true);
    ui->feel_nothing->setDisabled(true);
    ui->feel_something->setDisabled(true);
    ui->increase_five->setDisabled(false);
    ui->decrease_five->setDisabled(false);
    ui->increase_one->setDisabled(false);
    ui->decrease_one->setDisabled(false);

}

void MainWindow::on_feel_something_clicked()
{
    //File initializer for recording the results
    resultsFile = fopen(outputfilepath, "a");

    if (resultsFile == NULL) {
        printf("Error! opening file");
        getchar();
        // Program exits if the file pointer returns NULL.
        exit(1);
    }
    participant_id = ui->participant_id->text();
    //std::string parti = participant_id.toUtf8().constData();
    moisture_percent =ui->moisture_percent->text();
    partnumber= ui->part_no->currentText();
    //print participant number
    fprintf(resultsFile, "%s, ", participant_id.toStdString().c_str());
    //print moisture level
    fprintf(resultsFile, "%s, ", moisture_percent.toStdString().c_str());
    //print partnumber
    fprintf(resultsFile, "%s, ", partnumber.toStdString().c_str());
    //print signal number
    fprintf(resultsFile, "%d, ", tester_file_number);
    //print feeling number
    fprintf(resultsFile, "2\n");
    ui->feel_good->setDisabled(true);
    ui->feel_strong->setDisabled(true);
    ui->feel_nothing->setDisabled(true);
    ui->feel_something->setDisabled(true);
    ui->increase_five->setDisabled(false);
    ui->decrease_five->setDisabled(false);
    ui->increase_one->setDisabled(false);
    ui->decrease_one->setDisabled(false);
    tester_reaction.append(2);
}

void MainWindow::on_feel_good_clicked()
{
    //File initializer for recording the results
    resultsFile = fopen(outputfilepath, "a");

    if (resultsFile == NULL) {
        printf("Error! opening file");
        getchar();
        // Program exits if the file pointer returns NULL.
        exit(1);
    }
    participant_id = ui->participant_id->text();
    //std::string parti = participant_id.toUtf8().constData();
    moisture_percent =ui->moisture_percent->text();
    partnumber= ui->part_no->currentText();
    //print participant number
    fprintf(resultsFile, "%s, ", participant_id.toStdString().c_str());
    //print moisture level
    fprintf(resultsFile, "%s, ", moisture_percent.toStdString().c_str());
    //print partnumber
    fprintf(resultsFile, "%s, ", partnumber.toStdString().c_str());
    //print signal number
    fprintf(resultsFile, "%d, ", tester_file_number);
    //print feeling number
    fprintf(resultsFile, "3\n");
    ui->feel_good->setDisabled(true);
    ui->feel_strong->setDisabled(true);
    ui->feel_nothing->setDisabled(true);
    ui->feel_something->setDisabled(true);
    ui->increase_five->setDisabled(false);
    ui->decrease_five->setDisabled(false);
    ui->increase_one->setDisabled(false);
    ui->decrease_one->setDisabled(false);
    tester_reaction.append(3);
}

void MainWindow::on_feel_strong_clicked()
{
    //File initializer for recording the results
    resultsFile = fopen(outputfilepath, "a");

    if (resultsFile == NULL) {
        printf("Error! opening file");
        getchar();
        // Program exits if the file pointer returns NULL.
        exit(1);
    }
    participant_id = ui->participant_id->text();
    //std::string parti = participant_id.toUtf8().constData();
    moisture_percent =ui->moisture_percent->text();
    partnumber= ui->part_no->currentText();
    //print participant number
    fprintf(resultsFile, "%s, ", participant_id.toStdString().c_str());
    //print moisture level
    fprintf(resultsFile, "%s, ", moisture_percent.toStdString().c_str());
    //print partnumber
    fprintf(resultsFile, "%s, ", partnumber.toStdString().c_str());
    //print signal number
    fprintf(resultsFile, "%d, ", tester_file_number);
    //print feeling number
    fprintf(resultsFile, "4\n");
    ui->feel_good->setDisabled(true);
    ui->feel_strong->setDisabled(true);
    ui->feel_nothing->setDisabled(true);
    ui->feel_something->setDisabled(true);
    ui->increase_five->setDisabled(false);
    ui->decrease_five->setDisabled(false);
    ui->increase_one->setDisabled(false);
    ui->decrease_one->setDisabled(false);
    tester_reaction.append(4);
}


void MainWindow::on_finish_clicked()
{
    info << ui->participant_id->text();
    info << "Selection Record: \n";
    foreach(int x, tester_choice){
            info << x;
            info << " ";
        }
        info << "\n";
        info << "Reaction Record: \n";
        foreach(int y,tester_reaction){
            info << y;
            info << " ";
        }
        info << "\n";
    this->close();
}
