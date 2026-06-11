rm -rf reports/allure-results
rm -rf reports/allure-report
mkdir -p reports/allure-results
mkdir -p reports/allure-report

cp allure-config/* reports/allure-results/

pytest -m smoke \
--browser chromium \
--alluredir=reports/allure-results

allure serve reports/allure-results