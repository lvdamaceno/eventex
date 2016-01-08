# Eventex

Sistema de Eventos encomendado pela Morena

[![Build Status](https://travis-ci.org/lvdamaceno/eventex.svg?branch=master)](https://travis-ci.org/lvdamaceno/eventex)
[![Code Climate](https://codeclimate.com/repos/5689f7666b58a245c10008fb/badges/b81cd92d990e4ec680c8/gpa.svg)](https://codeclimate.com/repos/5689f7666b58a245c10008fb/feed)
[![Test Coverage](https://codeclimate.com/repos/5689f7666b58a245c10008fb/badges/b81cd92d990e4ec680c8/coverage.svg)](https://codeclimate.com/repos/5689f7666b58a245c10008fb/coverage)
[![Issue Count](https://codeclimate.com/repos/5689f7666b58a245c10008fb/badges/b81cd92d990e4ec680c8/issue_count.svg)](https://codeclimate.com/repos/5689f7666b58a245c10008fb/feed)

## Como desenvolver?

1. Clone o repositório.
2. Crie um virtualenv com Python 3.5
3. Ative o virtualenv.
4. Instale as dependencias.
5. Configure a instância com o .env
6. Execute os testes.

```console
git clone https://github.com/lvdamaceno/eventex.git wttd
cd wttd
python -m venv .wttd
source .wttd/bin/activate
pip install -r requirements-dev.txt
cp contrib/env-sample .env
python manage.py test
```

## Como fazer o deploy?

1. Crie uma instância no heroku.
2. Envie as configurações para o heroku.
3. Defina uma SECRETE_KEY segura para instância.
4. Defina DEBUG=False
5. Configure o serviço de email.
6. Envie o código para p heroku

```console
heroku create minhainstancia
heroku config:push
heroku config:set SECRET_KEY=`python contrib/secret_gen.py`
heroku config:set DEBUG=False
#configuro email
git push heroku master --force
```