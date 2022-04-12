from robot.api.deco import keyword
from robot.api.logger import info
from robot.libraries.BuiltIn import BuiltIn

from framework.utils.sqlmaster.sqlmaster import SQLMaster


class SQLSteps:

    @staticmethod
    @keyword(name="Connect To DB")
    def connect_to_db():
        login = BuiltIn().get_variable_value('${user}')
        password = BuiltIn().get_variable_value('${passwd}')
        sqlmaster = SQLMaster(login, password)
        return sqlmaster

    @staticmethod
    @keyword(name="Fetch All Games")
    def fetch_all_games(conn: SQLMaster):
        tables = conn.get_table_list()
        tables_content = [conn.fetch_all(i) for i in tables]
        info(f'Fetched from DB:\n{tables_content}')
        return tables_content

