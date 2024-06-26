функции менеджера паролей
========================= 
Первым шагом создаем файл password.py и терминале запускаем

.. code-block:: console

   (.venv) $ pip install cryptography

cryptography - это библиотека для шифрования 

Затем открываем файл Python и импортируем необходимые библиотеки:

.. code-block:: python

   import json, hashlib, getpass, os, sys
   from cryptography.fernet import Fernet

json — это библиотека для кодирования и декодирования данных JSON обычно используемая для сериализации и обмена данными (Сериализация (в программировании) — процесс перевода структуры данных в битовую последовательность).

hashlib— это библиотека, предоставляющая безопасные хэш-функции, включая SHA-256, для создания хэш-значений из данных, часто используемых для хеширования паролей и проверки целостности данных. 

getpass: библиотека для безопасного и интерактивного ввода конфиденциальной информации, например паролей, без отображения ввода на экране. Аналогично тому, как работают терминалы Linux.

os: библиотека для взаимодействия с операционной системой, позволяющая выполнять такие задачи, как манипулирование файлами и каталогами.

sys: этот модуль представляет собой встроенный модуль Python, который обеспечивает доступ к различным системным параметрам и функциям.

cryptography.fernet: Являясь частью библиотеки cryptography, он предоставляет метод шифрования с симметричным ключом Fernet для безопасного шифрования и дешифрования данных. 

После импорта необходимых библиотек создаем класс.Python имеет множество встроенных типов, например, int, str и так далее, которые мы можем использовать в программе. Но также Python позволяет определять собственные типы с помощью классов. Класс представляет некоторую сущность. Конкретным воплощением класса является объект. В языке Python класс определяется с помощью ключевого слова class:

1 . class название_класса:
2 . атрибуты_класса
3 . методы_класса

В данном случае определен класс Password, который условно представляет пароль. В данном случае в классе не определяется никаких методов или атрибутов. Однако поскольку в нем должно быть что-то определено, то в качестве заменителя функционала класса применяется оператор pass. Этот оператор применяется, когда синтаксически необходимо определить некоторый код, однако исходя из задачи код нам не нужен, и вместо конкретного кода вставляем оператор pass.

.. code-block:: python

   class Password:
      def __init__(self):
         pass


Далее рассмотрим функцию хеширования (Криптографическая хеш-функция — это алгоритм, который принимает на вход сообщение и превращает его в уникальный битовый массив фиксированного размера. Такой массив называется хешем, или хеш-суммой, а сам процесс — хешированием.Более подробно о процессе хеширования можно познакрмиться по ссылке https://skillbox.ru/media/code/kheshfunktsiya-chto-eto-dlya-chego-nuzhna-i-kak-rabotaet/ ). Эта функция будет использоваться для хеширования нашего главного пароля при регистрации:


.. code-block:: python


 def hash_password(self, password):
        sha256 = hashlib.sha256()
        sha256.update(password.encode())
        return sha256.hexdigest()

При определении методов любого класса, как и конструктора, первый параметр метода представляет ссылку на текущий объект, который согласно условностям называется self.

После этого создаем функцию генерации ключа. Этот ключ будет использоваться для шифрования наших паролей при добавлении и расшифровки при извлечении. Далее мы фернетим ключ (чтобы он мог шифровать и расшифровывать наши пароли) и создаем функции для шифрования и дешифрования:

.. code-block:: python

  # Generate a secret key. This should be done only once as you'll see.
    def generate_key(self):
        return Fernet.generate_key()

    # Initialize Fernet cipher with the provided key.
    def initialize_cipher(self, key):
        return Fernet(key)

    # Function to encrypt a  password.
    def encrypt_password(self, cipher, password):
        return cipher.encrypt(password.encode()).decode()

    # Function to decrypt a  password.
    def decrypt_password(self, cipher, encrypted_password):
        return cipher.decrypt(encrypted_password.encode()).decode()


После чего создаем функцию регистрации владельца. Сохранение учетных данных в user_data.json файле. 

.. code-block:: python

   # Function to register you.
    def register(self, username, master_password):
        # Encrypt the master password before storing it
        hashed_master_password = self.hash_password(master_password)
        user_data = {'username': username, 'master_password': hashed_master_password}
        file_name = 'user_data.json'
        if os.path.exists(file_name) and os.path.getsize(file_name) == 0:
            with open(file_name, 'w') as file:
                json.dump(user_data, file)
                print("\n[+] Registration complete!!\n")
        else:
            with open(file_name, 'x') as file:
                json.dump(user_data, file)
                print("\n[+] Registration complete!!\n")


Следующим этапом создаем функцию для входа пользователя в систему. Система принимает имя и пароль пользователя, а затем хэширует пароль, введенный пользователем. Если хэш введенного пароля совпадает с хешем сохраненного пароля (в файле JSON) и имена пользователей совпадают, доступ предоставляется. 

.. code-block:: python

   def login(username, entered_password):
      try:
          with open('user_data.json', 'r') as file:
              user_data = json.load(file)
          stored_password_hash = user_data.get('master_password')
          entered_password_hash = hash_password(entered_password)
          if entered_password_hash == stored_password_hash and username == user_data.get('username'):
              print("\n[+] Login Successful..\n")
          else:
              print("\n[-] Invalid Login credentials. Please use the credentials you used to register.\n")
              sys.exit()
      except Exception:
          print("\n[-] You have not registered. Please do that.\n")
          sys.exit()


Далее идет функция просмотра сайтов, сохраненных в менеджере паролей. При этом порядок записи функций не имеет особого значения. Важно в каком порядке мы их будем вызывать, (например, нельзя сохранить пароль пользователю который не имеет логин и т.д.):


.. code-block:: python

    def view_websites(self):
        try:
            with open('passwords.json', 'r') as data:
                view = json.load(data)
                print("\nWebsites you saved...\n")
                for x in view:
                    print(x['website'])
                print('\n')
        except FileNotFoundError:
            print("\n[-] You have not saved any passwords!\n")

Далее мы генерируем или загружаем наш ключ. 

.. code-block:: python

   def get_key(self):
           # Load or generate the encryption key.
           key_filename = 'encryption_key.key'
           if os.path.exists(key_filename):
               with open(key_filename, 'rb') as key_file:
                   key = key_file.read()
           else:
               key = self.generate_key()
               with open(key_filename, 'wb') as key_file:
                   key_file.write(key)
   
           cipher = self.initialize_cipher(key)
           return cipher


По сути, эта функция проверяет, существует ли файл encryption_key.key. Если существует, то он загружает его для использования. Если нет, он создает его и сохраняет в нем наш уникальный ключ. 
.. autosummary::
   :toctree: generated

  lumache
