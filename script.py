import random
from datacenter.models import Mark, Schoolkid, Chastisement, Lesson
from django.core.exceptions import MultipleObjectsReturned, ObjectDoesNotExist


def fix_marks(schoolkid):
    all_bad_marks = Mark.objects.filter(schoolkid=schoolkid, points__in=[2, 3])
    for mark in all_bad_marks:
        mark.points = 5
        mark.save()


def remove_chastisements(schoolkid):
    all_chastisement = Chastisement.objects.filter(schoolkid=schoolkid)
    for chastisement in all_chastisement:
        chastisement.delete()


def create_commendation(name, subject_title):
    try:
        schoolkid = Schoolkid.objects.get(full_name__contains=name)
    except  MultipleObjectsReturned:
        print("Есть несколько учеников с такой фамилией или именем, уточните вводимые данные")
    except ObjectDoesNotExist:
        print("Базе нет ученика с такой фамилией или именем, проверьте вводимые данные")

    first_lesson = Lesson.objects.filter(year_of_study=schoolkid.year_of_study,
                                         group_letter=schoolkid.group_letter,
                                        subject__title=subject_title).order_by('-date').first()

    chastisements = [
        "С каждым разом у тебя получается всё лучше!",
        "Мы с тобой не зря поработали!",
        "Я вижу, как ты стараешься!",
        "Ты растешь над собой!",
        "Ты многое сделал, я это вижу!",
        "Теперь у тебя точно все получится!"
    ]

    Chastisement.objects.create(text=random.choice(chastisements),
                                created=first_lesson.date,
                                schoolkid=schoolkid,
                                subject=first_lesson.subject,
                                teacher=first_lesson.teacher)



