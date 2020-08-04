import matrixbz.cache as cache

class TestCacheDecorators:
    def test_cache_result(self):
        @cache.cache_result
        def fake():
            pass
        assert fake.cache_result
