#include <iostream>
#include <stdio.h>
#include <conio.h>
#include <string> 
using namespace std;

const int N = 5;

class book {
public:
	string genre;
	string author;
	string name;
	int year;
	int price;
	book() {
		genre = " ";
		author = " ";
		name = " ";
		year = 0;
		price = 0;
	}
};

book knigi[N] = {};
int sch = 0;
int menu();
void enter_massiv();
void out_sort();
void change();

int menu() {
	int n;
	cout << "Введите:\n";
	cout << "1-для ввода массива\n";
	cout << "2-для вывода отсортированного массива структур\n";
	cout << "3-для изменения данных структуры\n";
	cout << "4-для окончания работы\n";
	cin >> n;
	cout << endl;
	return n;
}

void enter_massiv() {
	cout << "Максимум записей: " << N << endl;
	cout << "Сейчас записей: " << sch << endl;
	if (sch == N)
	{
		cout << "Введено максимум записей!" << endl;
		return;
	}
	else
	{
		cout << endl;
		cout << "Запись номер " << sch + 1;
		cout << "\nВведите жанр книги\n";
		getline(cin, knigi[sch].genre);
		getline(cin, knigi[sch].genre);
		cout << "\nВведите автора книги\n";
		getline(cin, knigi[sch].author);
		cout << "\nВведите назване книги\n";
		getline(cin, knigi[sch].name);
		cout << "\nВведите год издания\n";
		cin >> knigi[sch].year;
		cout << "\nВведите цену книги\n";
		cin >> knigi[sch].price;
		sch++;
	}
}


void out_sort() {
	int sw;
	if (sch == 0)
		cout << "\nНет запиcей: \n";
	else
	{
		cout << "Массив: \n";
		for (int i = 0; i < sch; i++)
		{
			for (int j = 0; j < sch - i; j++)
				if (knigi[j].genre < knigi[j + 1].genre)
				{
					string temp1 = knigi[j].genre;
					knigi[j].genre = knigi[j + 1].genre;
					knigi[j + 1].genre = temp1;
				}
		}
		for (int i = 0; i < sch; i++)
		{
			cout << endl;
			cout << "Выводится запись : " << i + 1 << endl;
			cout << "Жанр книги: " << knigi[i].genre << endl;
			cout << "Автор книги: " << knigi[i].author << endl;
			cout << "Название книги: " << knigi[i].name << endl;
			cout << "Год издания книги: " << knigi[i].year << endl;
			cout << "Цена книги: " << knigi[i].price << endl;
			cout << endl;
		}
	}
}

void change() {
	int numb;
	int per;
	if (sch == 0)
		cout << "\nНет запиcей: \n";
	else
	{
		cout << "\nВведите номер записи\n";
		cin >> numb;
		do
		{
			cout << "Введите: \n";
			cout << "1-для изменения жанра книги\n";
			cout << "2-для изменения автора книги\n";
			cout << "3-для изменения названия книги\n";
			cout << "4-для изменения года издания книги\n";
			cout << "5-для изменения года цены книги\n";
			cout << "6-для прекращения\n";
			cin >> per;
			switch (per)
			{
			case 1:
				cout << "Введите жанр книги\n";
				cin >> knigi[numb - 1].genre;
				break;
			case 2:
				cout << "Введите автора книги\n";
				cin >> knigi[numb - 1].author;
				break;
			case 3:
				cout << "Введите название книги \n";
				cin >> knigi[numb - 1].name;
				break;
			case 4:
				cout << "Введите год издания книги\n";
				cin >> knigi[numb - 1].year;
				break;
			case 5:
				cout << "Введите цену книги\n";
				cin >> knigi[numb - 1].price;
				break;
			case 6: return;
			}

		} while (1);
	}
}

int main( ) {
	setlocale(0, "Rus");
	while (1)
	{
		switch (menu())
		{
		case 1:
			enter_massiv();
			break;
		case 2:
			out_sort();
			break;
		case 3:
			change();
			break;
		case 4:
			return 0;
		default:
			cout << "Неверный выбор/n";
		}
	}
}

