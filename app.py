import streamlit as st

# Classe para representar uma Tarefa
class Task:
    def __init__(self, title, assignee=None, deadline=None):
        self.title = title
        self.assignee = assignee
        self.deadline = deadline
        self.status = "Pendente"
        self.tracked_time = 0  # Em minutos
    
    def update_status(self, new_status):
        self.status = new_status
    
    def track_time(self, minutes):
        self.tracked_time += minutes
    
    def __str__(self):
        return f"{self.title} - {self.status} (Responsável: {self.assignee}, Prazo: {self.deadline}, Tempo: {self.tracked_time} min)"

# Gerenciador de Tarefas
class TaskManager:
    def __init__(self):
        self.tasks = []
    
    def add_task(self, title, assignee=None, deadline=None):
        task = Task(title, assignee, deadline)
        self.tasks.append(task)
    
    def list_tasks(self):
        return self.tasks
    
    def update_task_status(self, title, new_status):
        for task in self.tasks:
            if task.title == title:
                task.update_status(new_status)
                return True
        return False
    
    def track_task_time(self, title, minutes):
        for task in self.tasks:
            if task.title == title:
                task.track_time(minutes)
                return True
        return False

# Criando instância do gerenciador de tarefas
tm = TaskManager()

# Interface Streamlit
st.title("Gerenciador de Tarefas")

# Adicionar Tarefa
title = st.text_input("Nome da Tarefa:")
assignee = st.text_input("Responsável:")
deadline = st.date_input("Prazo:")
if st.button("Adicionar Tarefa"):
    tm.add_task(title, assignee, str(deadline))
    st.success(f"Tarefa '{title}' adicionada!")

# Listar Tarefas
st.subheader("Tarefas Atuais")
for task in tm.list_tasks():
    st.write(str(task))

# Atualizar Status
task_to_update = st.text_input("Nome da tarefa para atualizar status:")
new_status = st.selectbox("Novo status:", ["Pendente", "Em andamento", "Concluído"])
if st.button("Atualizar Status"):
    if tm.update_task_status(task_to_update, new_status):
        st.success(f"Status atualizado para '{new_status}'!")
    else:
        st.error("Tarefa não encontrada.")

# Rastrear Tempo
task_to_track = st.text_input("Nome da tarefa para rastrear tempo:")
minutes = st.number_input("Minutos trabalhados:", min_value=0)
if st.button("Adicionar Tempo"):
    if tm.track_task_time(task_to_track, minutes):
        st.success(f"{minutes} minutos adicionados!")
    else:
        st.error("Tarefa não encontrada.")
