#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include "timer.h"
#include "826api.h"

namespace Ui {
class MainWindow;
}

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    explicit MainWindow(QWidget *parent = 0);
    ~MainWindow();

private slots:
    void on_increase_five_clicked();

    void on_decrease_five_clicked();

    void on_increase_one_clicked();

    void on_decrease_one_clicked();

    void on_feel_nothing_clicked();

    void on_play_clicked();

    void on_feel_good_clicked();

    void on_feel_strong_clicked();

    void on_finish_clicked();

    void on_feel_something_clicked();

private:
    Ui::MainWindow *ui;

};

#endif // MAINWINDOW_H
