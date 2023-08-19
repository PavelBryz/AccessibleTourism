from datetime import date, timedelta

from django.contrib.auth.models import User

from main_app.enums import Level
from words_operations.models import MostMisspelledWords, UsersWords, Words, WordAddType

def fill_mmw_for_user(user_id: int):
    mmw = MostMisspelledWords.objects.order_by("?").all()
    auto = WordAddType.objects.get(type='Automatic')
    user = User.objects.get(id=user_id)
    step = 5
    steps = 0
    start = 0
    words = []
    while mmw[start: start + step]:
        for word in mmw[start: start + step]:
            words.append(UsersWords(user_id=user,
                                    word_id=word.word,
                                    next_repeat_date=date.today() + timedelta(days=steps),
                                    level=Level.ZERO.value,
                                    add_type=auto))

        start += step
        steps += 1

    UsersWords.objects.bulk_create(words)


if __name__ == '__main__':
    mmw = MostMisspelledWords.objects.all()
    print(mmw)