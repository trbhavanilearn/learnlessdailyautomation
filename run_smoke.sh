rm -rf reports/allure-results
mkdir -p reports/allure-results

cp allure-config/* reports/allure-results/

pytest -m smoke \
--browser chromium \
--alluredir=reports/allure-results

allure serve reports/allure-results