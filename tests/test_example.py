def test_first(driver):
    driver.get(driver.base_url)
    assert "Яндекс" in driver.title
