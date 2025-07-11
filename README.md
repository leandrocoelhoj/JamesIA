# JamesIA

JamesIA é um projeto de automação e orquestração de workflows utilizando **Apache Airflow**, **Selenium**, **Docker** e **Celery**. O objetivo principal é automatizar processos de provisionamento, raspagem de dados e integração com sistemas de discadores (Callix, Ipbox, Vonix).

## 🚀 Principais Funcionalidades

* **Automação Web** com Selenium para interagir em sistemas de discagem.
* **Orquestração de DAGs** no Airflow: agendamento e monitoramento de tarefas.
* **Executor Celery** distribuído com Redis como broker e PostgreSQL como backend de resultados.
* **Containerização** com Docker para isolamento e facilidade de deploy.
* **Configuração via variáveis de ambiente** e `.env` para segurança de credenciais.
* **DAGs de exemplo** e scripts de bootstrap para inicialização do Airflow.

## 📦 Estrutura do Projeto

```
JamesIA/
├── airflow/                # Configuração do Airflow
│   ├── config/             # Arquivo airflow.cfg e arquivos relacionados
│   ├── dags/               # Diretório de DAGs do Airflow
│   ├── plugins/            # Plugins customizados
│   └── logs/               # Logs gerados pelo Airflow
├── scripts/                # Scripts de inicialização (airflow-init.sh)
├── src/                    # Código principal em Python
│   ├── auth/               # Módulos de autenticação e factories
│   ├── automations/        # Lógica de automação (Callix, Ipbox, ...)
│   ├── config/             # Definições de configurações (env, .env)
│   ├── core/               # Classes e utilitários base (BasePage, etc.)
│   └── pages/              # Páginas e mapeamentos de XPaths
├── Dockerfile              # Imagem customizada baseada em apache/airflow
├── docker-compose.yaml     # Definição de serviços (Airflow, Redis, Postgres)
├── requirements.txt        # Dependências Python (pip)
├── .env.example            # Exemplo de variáveis de ambiente
└── README.md               # Este documento
```


## ⚙️ Configuração

1. **Copie** o arquivo de exemplo de variáveis de ambiente:

   ```bash
   cp .env.example .env
   ```
2. **Edite** `.env` para ajustar as credenciais de banco, sistemas e usuário do Airflow.
3. **(Opcional)** Adicione credenciais de Selenium / ChromeDriver, se necessário.

## 🐳 Construção da Imagem

Primeiro fazer o build da imagem pra depois subir os serviços que vão utilizar essa imagem.

```bash
docker build -t jamesia/airflow:3.0.0-selenium .
```

## 🚀 Executando com Docker Compose

Basta chamar:

```bash
docker compose up -d
````

Isso iniciará os serviços:

* `airflow-apiserver` (porta 8080)
* `airflow-scheduler`
* `airflow-triggerer`
* `airflow-worker` (Celery)
* `airflow-dag-processor`
* `postgres` (porta 5432)
* `redis` (porta 6379)

Para parar e remover containers:

```bash
docker compose down
```

## 🔍 Testando Imports no Container

Para validar que o código em `src/` está acessível dentro do Airflow:

```bash
docker exec -it <scheduler_container> bash
python -c "from src.automations.callix.callix import executar_callix"
```

Se não houver erro, os imports estão configurados corretamente.

## 📚 Desenvolvendo Novos DAGs

1. Crie um arquivo `.py` em `airflow/dags/`.
2. Importe módulos de `src/`:

   ```python
   from src.automations.callix.callix import executar_callix
   ```
3. Defina sua DAG, tarefas e dependências.
4. Aguarde o scheduler carregar ou reinicie com:

   ```bash
   docker compose restart airflow-scheduler
   ```


## 🤝 Contribuição

1. Fork do repositório
2. Crie uma branch feature: `git checkout -b feature/nova-dag`
3. Commit das alterações: `git commit -m "feat: descrição"`
4. Push para branch: `git push origin feature/nova-dag`
5. Abra um Pull Request
