import gzip
import delegator
with gzip.open('backup.gz', 'wb') as f:
    c = delegator.run('pg_dump PGPASSWORD=wZWG0OmRbh73d3dMdk0OvrUZ0Xq02RI1 psql -h dpg-chma7ag2qv27ib60utog-a.singapore-postgres.render.com -U fruitshop_user fruitshop')
    f.write(c.out.encode('utf-8'))