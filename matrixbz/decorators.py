import functools
from .bot import Bot

def matrixbz_method(func):
    '''Methods with this decorator will be invocable as a bot command:
       !<bot_name> <method_name> <args>
    '''
    func.matrixbz_method = True
    @functools.wraps(func)
    async def wrapped(*args, **kwargs):
        return await func(*args, **kwargs)
    return wrapped

def matrixbz_msg_handler(func):
    '''A Method with this decorator will handle all message events received by the bot.
       A context object with room and client objects will be passed in.
       Bot creation will throw if more than one method is marked.
    '''
    func.matrixbz_msg_handler = True
    @functools.wraps(func)
    async def wrapped(*args, **kwargs):
        return await func(*args, **kwargs)
    return wrapped

def matrixbz_startup_method(func):
    '''The Method marked with this decorator will be run once the bot logs in.
       The async client will be passed in.
       Bot creation will throw if more than one method is marked.
    '''
    func.matrixbz_startup_method = True
    @functools.wraps(func)
    async def wrapped(*args, **kwargs):
        return await func(*args, **kwargs)
    return wrapped


def matrixbz_controller(bot_name, channel_greeting=None):
    '''Marks a class to generate a matrix bot.
       Marked class will get a create_matrix_bot method that will create a Bot instance.
    '''

    def matrixbz_controller_wrapper(cls):
        cls.matrixbz_controller = True
        cls.MATRIXBZ_BOT_NAME = bot_name
        cls.CHANNEL_GREETING = channel_greeting

        @staticmethod
        def create_matrix_bot(creds):
            controller = cls()
            return Bot(controller, creds)
        cls.create_matrix_bot = create_matrix_bot
        return cls
    return matrixbz_controller_wrapper
