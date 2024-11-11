from sqlalchemy import JSON, select
from sqlalchemy import type_coerce
from sqlalchemy.dialects import mysql
import json

# Иногда необходимо, чтобы SQLAlchemy знал тип данных выражения, по всем указанным выше причинам, но не отображал
# само выражение CAST на стороне SQL, где оно может помешать операции SQL, которая уже работает без него.
# Для этого довольно распространенного варианта использования есть другая функция, type_coerce() которая тесно
# связана с cast(), в том смысле, что она устанавливает выражение Python как имеющее определенный тип базы данных SQL,
# но не отображает CAST ключевое слово или тип данных на стороне базы данных. type_coerce() особенно важно при
# работе с JSON типом данных, который обычно имеет сложную связь со строковыми типами данных на разных платформах и
# может даже не быть явным типом данных, например, на SQLite и MariaDB. Ниже мы используем type_coerce() для передачи
# структуры Python в виде строки JSON в одну из функций JSON MySQL:

from sqlalchemy import JSON
from sqlalchemy import type_coerce
from sqlalchemy.dialects import mysql
s = select(type_coerce({"some_key": {"foo": "bar"}}, JSON)["some_key"])
print(s.compile(dialect=mysql.dialect()))

# JSON_EXTRACT Выше была вызвана функция SQL MySQL, поскольку мы использовали type_coerce() ее для указания того,
# что наш словарь Python следует рассматривать как JSON. В этом случае __getitem__ оператор Python ['some_key']
# стал доступен в результате и позволил отобразить JSON_EXTRACT выражение пути
# (не показано, однако в этом случае это в конечном итоге будет '$."some_key"').
