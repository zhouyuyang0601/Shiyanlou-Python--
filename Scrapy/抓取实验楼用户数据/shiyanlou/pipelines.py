from datetime import datetime
from sqlalchemy.orm import sessionmaker
from shiyanlou.models import Course, User, engine
from shiyanlou.items import CourseItem, UserItem


class ShiyanlouPipeline(object):

    def process_item(self, item, spider):
        """ ???? item ?????????
        """
        if isinstance(item, CourseItem):
            self._process_course_item(item)
        else:
            self._process_user_item(item)
        return item

    def _process_course_item(self, item):
        item['students'] = int(item['students'])
        self.session.add(Course(**item))

    def _process_user_item(self, item):
        # ???????? 'L100'????? 'L' ????? int
        item['level'] = int(item['level'][1:])
        # ???????? '2017-01-01 ?????'
        # ???????????? date ??
        item['join_date'] = datetime.strptime(item['join_date'].split()[0], '%Y-%m-%d').date()
        # ????????? int
        item['learn_courses_num'] = int(item['learn_courses_num'])
        # ??? session
        self.session.add(User(**item))

    def open_spider(self, spider):
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def close_spider(self, spider):
        self.session.commit()
        self.session.close()

