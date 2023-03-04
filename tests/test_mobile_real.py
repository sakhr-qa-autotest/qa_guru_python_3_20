import allure
from allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import have
from selene.support.shared import browser


@allure.title('Test search')
def test_search():
    with step('Skip'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_skip_button')).click()
    with step('Test search'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, 'Поиск по Википедии')).click()
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/search_src_text')).type('QA')
        browser.element((AppiumBy.XPATH,
                         '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout[1]/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]/android.widget.TextView[1]')).should(
            have.text('QA'))
    with step('Test go to page'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title')).click()
    with step('Text button "GO BACK"'):
        browser.element((AppiumBy.XPATH, '//android.widget.ImageButton[@content-desc="Перейти вверх"]')).click()
        browser.element((AppiumBy.XPATH, '//android.widget.ImageButton[@content-desc="Перейти вверх"]')).click()
        browser.element((AppiumBy.CLASS_NAME, 'android.widget.TextView')).should(have.text('Поиск по Википедии'))
