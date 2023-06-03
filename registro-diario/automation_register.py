import datetime
import discord

# Criando as listas de tarefas
tarefas_recorrentes = [
]
tarefas_ontem = []
tarefas_hoje = []
tarefas_amanha = []

msg = ""

# Criando um dicionário para tradução do dia da semana
dia_semana = {
    0: 'Domingo',
    1: 'Segunda',
    2: 'Terça',
    3: 'Quarta',
    4: 'Quinta',
    5: 'Sexta',
    6: 'Sábado'
}

class MyClient(discord.Client):
    def __init__(self, msg, *args, **kwargs):
        intents = discord.Intents.default()
        super().__init__(intents=intents, *args, **kwargs)
        print(f'Mensagem:\n{msg}')
        self.message = msg

    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
        channel_id = 1114202890370822144
        await self.send_message(channel_id, self.message)
        await self.close()

    async def send_message(self, channel_id, msg):
        channel = self.get_channel(channel_id)
        if channel is not None:
            print(f'Sending message to channel: {channel.name}')
            print(f'Mensagem:\n{msg}')
            await channel.send(msg)
        else:
            print(f'No channel with id {channel_id} found.')

# Lendo as informações do arquivo de texto
with open('tarefas.txt', 'r') as file:
    lines = file.readlines()

for line in lines:
    line = line.strip()
    if line.startswith('Recorrentes:'):
        tarefas_recorrentes.append('-' + line[12:])
    elif line.startswith('Ontem:'):
        tarefas_ontem.append('-' + line[6:])
    elif line.startswith('Hoje:'):
        tarefas_hoje.append('-' + line[5:])
    elif line.startswith('Amanha:'):
        tarefas_amanha.append('-' + line[7:])



# Solicitando ao usuário para inserir o dia atual e Nome
print("\n")

dia_atual = int(input("Digite o dia atual:\n1 para Segunda\n2 para Terça\n3 para Quarta\n4 para Quinta\n5 para Sexta\n"))
nome = input('Seu nome: ')

data = datetime.date.today()
print(f"== Daily report - {data.strftime('%d/%m/%Y')} ==")
msg += "\n\n"
msg += f"== Daily report - {data.strftime('%d/%m/%Y')} ==\n\n"
msg += f"== Nome: {nome} ==\n\n"


# Para cada dia a partir de ontem até amanhã
for i in range(-1, 2):

    if i == -1:
        if(dia_semana[(dia_atual - 1) % 7] == "Domingo"):
            print(f"\nSexta - Semana Passada")
            msg += f"\nSexta - Semana Passada"
        else:
            print(f"\n{dia_semana[(dia_atual - 1) % 7]} - Ontem")
            msg += f"\n{dia_semana[(dia_atual - 1) % 7]} - Ontem"
        tarefas = tarefas_ontem
    elif i == 0:
        print(f"\n{dia_semana[dia_atual]} - Hoje")
        msg += f"\n{dia_semana[dia_atual]} - Hoje"
        tarefas = tarefas_hoje
    else:
        if(dia_semana[(dia_atual + 1) % 7] == "Sábado"):
            print(f"\nSegunda - Próxima Semana")
            msg += f"\nSegunda - Próxima Semana"
        else:
            print(f"\n{dia_semana[(dia_atual + 1) % 7]} - Amanhã")
            msg += f"\n{dia_semana[(dia_atual + 1) % 7]} - Amanhã"

        tarefas = tarefas_amanha

    print("Daily report - 🔃 ✅")
    msg += "\nDaily report - 🔃 ✅\n\n"

    # Escrevendo as tarefas recorrentes
    for tarefa in tarefas_recorrentes:
        msg += tarefa + "\n"

    # Escrevendo as tarefas
    for tarefa in tarefas:
        msg += tarefa + "\n"

    print("\n")

print("\n\n")
print("--- \n ✅  Concluída!   |   🏃  Em execução!   |   🚫  Bloqueada!   |   🆕  Não planejada!   |   ⏱️  Não iniciada!   |   🔃  Recorrente!")
msg += ("--- \n ✅  Concluída!   |   🏃  Em execução!   |   🚫  Bloqueada!   |   🆕  Não planejada!   |   ⏱️  Não iniciada!   |   🔃  Recorrente!")

client = MyClient(msg)
token = 'MTExNDE2OTYzNzY0MzUwNTY3NA.GLgmkL.0WAvNWcpYSEPOWggdQUaxpH73eD8dmhFfrNJy4'

client.run(token)
