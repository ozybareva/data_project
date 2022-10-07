import env_file
import os
from pathlib import Path

base_dir = Path(__file__).parent.parent.absolute()


class Settings:

    env_file.load(f'{base_dir}/.env')

    db_postgres_host: str = os.environ.get('DB_POSTGRES_HOST')
    db_postgres_port: int = os.environ.get('DB_POSTGRES_PORT')
    db_postgres_user: str = os.environ.get('DB_POSTGRES_USER')
    db_postgres_pass: str = os.environ.get('DB_POSTGRES_PASS')
    db_postgres_name: str = os.environ.get('DB_POSTGRES_NAME')

    @property
    def postgres_dsn(self) -> str:
        return 'postgres://{}:{}@{}:{}/{}'.format(
            self.db_postgres_user,
            self.db_postgres_pass,
            self.db_postgres_host,
            self.db_postgres_port,
            self.db_postgres_name
        )
