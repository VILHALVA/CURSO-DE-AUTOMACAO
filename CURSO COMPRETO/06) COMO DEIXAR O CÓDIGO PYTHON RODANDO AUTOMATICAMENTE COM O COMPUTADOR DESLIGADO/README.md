# COMO DEIXAR O CÓDIGO PYTHON RODANDO AUTOMATICAMENTE COM O COMPUTADOR DESLIGADO?
Para executar um código Python automaticamente, mesmo quando o computador está desligado, você precisa criar um serviço ou tarefa agendada que seja executado em segundo plano. Isso pode ser feito dependendo do sistema operacional que você está usando. Vou explicar como fazer isso em sistemas Windows e Linux:

**No Windows:**

Você pode criar uma tarefa agendada usando o "Agendador de Tarefas" do Windows. Siga estas etapas:

1. Pressione "Win + S" e pesquise por "Agendador de Tarefas" ou encontre-o no "Painel de Controle".

2. No "Agendador de Tarefas", clique em "Criar Tarefa Básica" no painel direito.

3. Siga o assistente para criar uma tarefa agendada. Defina o nome e a descrição da tarefa.

4. Na guia "Disparadores", defina quando deseja que a tarefa seja executada (por exemplo, "Iniciar tarefa na inicialização").

5. Na guia "Ações", escolha "Iniciar um programa" e selecione o caminho para o executável Python e seu arquivo Python que deseja executar.

6. Configure outras opções, como a frequência da execução e as condições, conforme necessário.

7. Conclua o assistente.

Agora, a tarefa será executada automaticamente, mesmo quando o computador estiver desligado. Certifique-se de que o computador não esteja configurado para hibernação ou suspensão, pois isso pode interromper a execução da tarefa.

**No Linux:**

Em sistemas Linux, você pode criar um serviço usando Systemd, que permite iniciar automaticamente um processo em segundo plano durante a inicialização. Siga estas etapas:

1. Crie um arquivo de serviço no diretório `/etc/systemd/system/`. Por exemplo, crie um arquivo chamado `meu_servico.service`:

```bash
sudo nano /etc/systemd/system/meu_servico.service
```

2. Adicione o seguinte conteúdo ao arquivo de serviço, substituindo o caminho para o executável Python e o caminho para o seu script Python:

```
[Unit]
Description=Meu serviço Python

[Service]
ExecStart=/usr/bin/python3 /caminho/para/seu_script.py
Restart=always
User=seu_usuario

[Install]
WantedBy=multi-user.target
```

Certifique-se de que o caminho para o executável Python (`/usr/bin/python3`) e o caminho para o seu script Python estejam corretos.

3. Salve o arquivo e saia do editor.

4. Habilite o serviço e inicie-o:

```bash
sudo systemctl enable meu_servico
sudo systemctl start meu_servico
```

Agora, o serviço será iniciado automaticamente durante a inicialização e continuará sendo executado em segundo plano, mesmo quando o computador estiver desligado.

Lembre-se de que, em ambas as abordagens, você deve garantir que o seu código Python não tenha erros que possam causar problemas de execução indefinida. Além disso, gerencie a saída e os logs adequadamente para monitorar o status do seu serviço ou tarefa agendada.