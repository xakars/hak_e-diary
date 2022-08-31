# hak_e-diary

Скрипт позволяет редактировать электронный дневник школы.

## Как пользоваться?
Прежде чем начать "хакать" электронный дневник школы, необходимо положить скрипт script.py в папку с проектом электронного дневника. Далее запустить shell командой:
```console
python3 manage.py shell
```
Импортировать скрипт в shell:(вставить команду в консоль)
```console
from primer import *
```
Прежде чем начать использование следующих функций, необходимо взять из базы учетку ученика, для этого воспользуйтесь командой:(где name - Фамилия и Имя ученика)
```console
schoolkid = Schoolkid.objects.get(full_name__contains='name')
``` 
При необходимости использовать следующие фукции:
1. fix_marks(schoolkid) - позволяет исправить плохие оценки(2, 3) на отлично, где schoolkid учетка ученика.
```console
fix_marks(schoolkid)
```
2. remove_chastisements(schoolkid) - позволяет удалить все замечания на ученика.
```console
remove_chastisements(schoolkid)
```
3. create_commendation() - позволяет создать положительные замечания. Пример использования:
```console
create_commendation('Иван', 'История')
```
