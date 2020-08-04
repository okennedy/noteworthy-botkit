import matrixbz

class TestDecorators:

    def test_matrixbz_method_(self):
        @matrixbz.matrixbz_method
        def fake():
            pass
        assert fake.matrixbz_method

    def test_matrixbz_msg_handler(self):
        @matrixbz.matrixbz_msg_handler
        def fake():
            pass
        assert fake.matrixbz_msg_handler

    def test_matrixbz_startup_method(self):
        @matrixbz.matrixbz_startup_method
        def fake():
            pass
        assert fake.matrixbz_startup_method

    def test_matrixbz_controller(self):
        bot_name = 'fakebot'
        greeting = 'fake greeting!'

        @matrixbz.matrixbz_controller(bot_name, channel_greeting = greeting)
        class Fake:
            pass
        pass

        assert Fake.matrixbz_controller
        assert Fake.MATRIXBZ_BOT_NAME == bot_name
        assert Fake.CHANNEL_GREETING == greeting

        assert Fake.create_matrix_bot
        fake_creds = {
            'homeserver': 'fake.im',
            'user': '@fake:fake.im',
            'password': 'fake'
        }
        bot = Fake.create_matrix_bot(fake_creds)
        assert bot
