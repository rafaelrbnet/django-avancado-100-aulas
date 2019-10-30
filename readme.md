**Curso django-avancado-100-aulas**  
https://www.udemy.com/course/django-avancado-100-aulas/

Aula 4  
`# TODO este é um comentário para ser feito no fututo`  
`# FIXME esta é uma correção para ser feita no futuro`  
  
Aula 5  
import pdb; pdb.set_trace()  
n (next): vai para a próxima linha  
c (continue): continua para o final ou pra o próximo breakpoint
l (list): mostra o código fonte do método e em que linha o cursus se encontra

Aula 8  
Class Based Views CBD  
Documentação do Django: https://docs.djangoproject.com/en/2.2/ref/class-based-views/

Aula 9  
ListViews: O django porcura automaticamente o nome dos templates de cada método.   
Ex: Classe: `class PersonList(ListView):` Model: `model = Person` o nome do template automaticamente é declarado e deve ser salvo em `clientes/templates/clientes/pperson_list.html`  
Paginação: Na view deve ser declarada `paginate_by = 1`  
No template:
```
{% if is_paginated %}
    <div class="pagination">
        <span class="page-links">
            {% if page_obj.has_previous %}
                <a href="/clientes/list?page={{ page_obj.previous_page_number }}">anterior</a>
            {% endif %}
            <span class="page-current">
                Página {{ page_obj.number }} de {{ page_obj.paginator.num_pages }}.
            </span>
            {% if page_obj.has_next %}
                <a href="/clientes/list?page={{ page_obj.next_page_number }}">próximo</a>
            {% endif %}
        </span>
    </div>
{% endif %}
```
            
 Aula 10  
 DetailViews:Mesmo padrão de nomenclatura de templates
 
 