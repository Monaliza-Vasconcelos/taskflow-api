from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Task

class TaskTests(APITestCase):

    def setUp(self):
        # Prepara um usuário autenticado
        self.user = User.objects.create_user(username='admin', password='123')
        self.client.force_authenticate(user=self.user)
        
        # Criando a tarefa inicial com o campo CORRETO: completed
        self.task = Task.objects.create(
            title="Tarefa de Teste",
            description="Descrição inicial",
            completed=False 
        )

    def test_create_task(self):
        """Testa o POST (Criar)"""
        url = reverse('task-list')
        data = {'title': 'Estudar Django', 'description': 'Completar o desafio'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_tasks(self):
        """Testa o GET (Listar todas)"""
        url = reverse('task-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_get_single_task(self):
        """Testa o GET por ID (Buscar uma específica)"""
        url = reverse('task-detail', kwargs={'pk': self.task.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], "Tarefa de Teste")

    def test_update_task(self):
        """Testa o PATCH/PUT (Atualizar)"""
        url = reverse('task-detail', kwargs={'pk': self.task.id})
        # Usando completed aqui também
        data = {'title': 'Título Alterado', 'completed': True}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        self.task.refresh_from_db()
        self.assertEqual(self.task.title, 'Título Alterado')
        self.assertTrue(self.task.completed)

    def test_delete_task(self):
        """Testa o DELETE (Remover)"""
        url = reverse('task-detail', kwargs={'pk': self.task.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Task.objects.count(), 0)