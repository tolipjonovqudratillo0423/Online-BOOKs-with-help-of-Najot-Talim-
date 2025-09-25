from .connect import get_connect

def create_important_table():
    first_connect_sql = """
    create table if not exists users(
        id bigserial primary key,
        chat_id bigint not null unique,
        username varchar(100)not null unique,
        phone varchar(100) not null unique,
        address varchar(100) not null,
        is_admin boolean)default False);
    
    create table if not exsist books(
        id bigserial primary key,
        title varchar(100) not null unique,
        author varchar(100) not null,
        description text,
        quantity integer default 1,
        price integer not null
    );
    
    create table if not exists orders(
        id bigserial primary key,
        user_id bigint references users(id),
        book_id bigint references books(id),
        status varchar(100) default 'new',
        quantity integer default 1,
        created_at timestamp default now(),
        updated_at timestamp default now());
        """
    with get_connect() as connect:
        with connect.cursor() as cursor:
            cursor.execute(first_connect_sql)
             
create_important_table()