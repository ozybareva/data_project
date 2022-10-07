create table aerich
(
    id      serial
        primary key,
    version varchar(255) not null,
    app     varchar(100) not null,
    content jsonb        not null
);

alter table aerich
    owner to oz66;

