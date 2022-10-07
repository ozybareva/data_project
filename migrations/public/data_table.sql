create table data_table
(
    id                          serial
        primary key,
    "ID_UCH_VOST_POL"           integer          not null,
    "NAME_BEGIN_VOST_UCH"       varchar(25)      not null,
    "ESR_BEGIN_VOST_UCH"        integer          not null,
    "DOR_BEGIN_VOST_UCH"        integer          not null,
    "OKATO_BEGIN_VOST_UCH_NAME" varchar(100)     not null,
    "X_BEG_VOST_UCH"            double precision not null,
    "Y_BEG_VOST_UCH"            double precision not null,
    "NAME_END_VOST_UCH"         varchar(25)      not null,
    "ESR_END_VOST_UCH"          integer          not null,
    "DOR_END_VOST_UCH"          integer          not null,
    "OKATO_END_VOST_UCH_NAME"   varchar(100)     not null,
    "X_END_VOST_UCH"            double precision not null,
    "Y_END_VOST_UCH"            double precision not null,
    "NUM_CNSI_MELK_SET"         integer          not null,
    "NAME_BEGIN_MELK_SET"       varchar(29)      not null,
    "ESR_BEGIN_MELK_SET"        integer          not null,
    "DOR_BEGIN_MELK_SET"        integer          not null,
    "OKATO_BEGIN_MELK_SET_NAME" varchar(100)     not null,
    "NAME_END_MELK_SET"         varchar(29)      not null,
    "ESR_END_MELK_SET"          integer          not null,
    "DOR_END_MELK_SET"          integer          not null,
    "OKATO_END_MELK_SET_NAME"   varchar(100)     not null
);

alter table data_table
    owner to oz66;

