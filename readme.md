<h3>Тестирование игры kkrieger.</h3>

Перед запуском необходимо установить зависимости:<br>
pip install -r requirements.txt

Для записи статистики использовался сторонний софт, который можно скачать по ссылке:<br>
https://fpsmon.com/ru/
После установки и запуска программы FPS Monitor необходимо:
<ol>
<li>В появившемся диалоговом окне можно выбрать "Попробовать демо-версию"</li>
<li>Зайти в меню "Настройки";</li>
<li>Выбрать "Расширение Benchmark";</li>
<li>Выбрать "Клавишу включения/выключения" - "8";</li>
<li>В поле "Файл для записи результатов" указать каталог, куда будет сохранена статистика;</li>
<li>Чекбокс "Добавить имя процесса и дату/время" должен быть пустым;</li>
<li>Сенсоры можно выбать любые, но первым из них должен быть "FPS";</li>
<li>ОК</li>
</ol>

FPS Monitor должен быть запущен.
Скрипт запускается из терминала командой:<br>
python run.py <path\to\kkrieger> -o <path\to\output> 

<b>Важно!</b><br>
<path\to\output> должен быть таким же, как путь, указанный в п.5 настройки программы FPS Monitor.

