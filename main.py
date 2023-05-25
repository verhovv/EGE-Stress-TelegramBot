import asyncio
from aiogram import Bot, Dispatcher, types
import stress

bot = Bot(token="6235485557:AAEVOA45ldBLt2ivtqscHIeLY47YU4VOvTQ")
dp = Dispatcher()


@dp.message()
async def message_handler(message: types.Message):
    await send_random_quiz(message.from_user.id)


@dp.poll_answer()
async def answer(PollAnswer: types.PollAnswer):
    await send_random_quiz(PollAnswer.user.id)


async def send_random_quiz(user_id: int):
    quiz = stress.get_random_quiz()

    await bot.send_poll(chat_id=user_id,
                        question=f'Поставь правильное ударение в слове {quiz.question.upper()}',
                        options=quiz.options,
                        type='quiz',
                        correct_option_id=quiz.correct_number,
                        is_anonymous=False)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
