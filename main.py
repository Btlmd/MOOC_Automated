import selenium.webdriver as wd
from selenium.webdriver.common.by import By
from time import sleep as slp
from tqdm import tqdm
from sys import argv

def sleep(seconds: int):
    print('wait %ds' % seconds)
    slp(seconds)

def time_to_seconds(desc: str) -> int:
    return int(desc[:2]) * 3600 + int(desc[3:5]) * 60 + int(desc[6:])

def url_update(url: str) -> str:
    spl = url.split('/')
    spl[-1] = str(int(spl[-1]) + 1)
    return '/'.join(spl)

class mooc_cracker(object):
    def __init__(self):
        if len(argv) >= 2 and argv[1] == '--chrome':
            self.d = wd.Chrome()
        else:
            self.d = wd.Firefox()

        self.d.maximize_window()
        self.d.implicitly_wait(0.5)

    def begin(self):
        self.d.get('https://tsinghua.yuketang.cn/')
        input('Login and get to the first page to play\nNOTE: The video page to be the ONLY page.')
        self.d.switch_to.window(self.d.window_handles[0])

    def get_time(self) -> list:
        eles = self.d.find_elements(By.XPATH, '//xt-time//span')
        return [time_to_seconds(i.get_attribute('innerHTML')) for i in eles]

    def finish_bar(self) -> bool:
        bar = self.d.find_elements(By.XPATH, '//div[@class="el-tooltip item"]/span')
        if len(bar):
            try:
                percentage = int(bar[0].text.replace('完成度：', '').replace('%', ''))
            except:
                return False
            if percentage >= 98:
                return True
        return False

    def check_status(self):
        while True:
            sleep(10)
            times = self.get_time()
            buttons = self.d.find_elements(By.XPATH,'//span/span[contains(@class, "f14") and contains(@class, "color6")]')
            title = self.d.find_elements(By.XPATH, '//div[@class="title-fl"]/span')
            title = title[0].text if len(title) else ' - '
            if len(times) == 2:
                # 视频态
                with tqdm(total=times[1], bar_format='{l_bar}{bar}', desc=title) as bar:
                    curr = times[0]
                    bar.update(curr)
                    play_stop = self.d.find_elements(By.CLASS_NAME, 'xt_video_bit_play_btn')
                    if len(play_stop) != 0:
                        if play_stop[0].is_displayed():
                            play_stop[0].click()
                    while True:
                        if self.finish_bar():
                            break

                        if times[1] - times[0] <= 1:
                            break

                        times = self.get_time()
                        bar.update(times[0] - curr)
                        curr = times[0]
                        slp(3)

            slp(4)

            has_next_flag = False
            for p_ele in buttons:
                if p_ele.get_attribute('innerHTML') == '下一单元':
                    self.d.get(url_update(self.d.execute_script('return window.location.href')))
                    print(title, 'done')
                    has_next_flag = True
                    break

            if has_next_flag:
                continue
            else:
                print('All done, have fun!')
                return

    def crack(self):
        self.begin()
        self.check_status()

c = mooc_cracker()
c.crack()

