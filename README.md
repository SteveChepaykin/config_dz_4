Вариант 28.

Ассмеблер и интерпретатор для учебной ВМ. Команды передаются в файле .txt формате A B C (команда текстом, ячейка памяти, операнд) Поддерживаемый список команд:
- загрузка константы (CONST). Загружает C в регистр с адресом B
- запись в память (PUT_MEM). Загружает информацию регистра B по адресу, сохраненному в регистре C
- чтение из памяти (GET_MEM). Загружает в регистр C информацию, находящуюся в памяти по адресу сохраненному в регистре B
- унарный минус (NEG). Выполняет операцию унарный минус над значением, сохраненным в памяти по значению из регистра B, и записывает в память по адресу, лежащему в регистре С.

Для запуска программы необходимо создать файл формата .txt и записать в нем список команд для выполнения, каждую с новой строки. Для примера предоставлен файл test.txt. Затем необходимо запустить файл main.py, и в стандартном вводе предоставить имя файла с командами.

Логирование представлено файлом log.xml, выходной файл - out.xml (формат .xml выбран согласно условию индивидуального задания).
