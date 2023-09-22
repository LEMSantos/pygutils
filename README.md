pygutils
========

Instalação
----------

Eu recomendo a instalação utilizando o `pipenv` ou o `virtualenv` para permitir um gerenciamento melhor das dependências.

```bash
pipenv install pygutils
```

ou

```bash
pip install pygutils
```

Conteúdo
--------

- [Animation](#animation)
- Camera
- [Event](#event)
- [Timer](#timer)


<div id="animation" />

### Animation -- [Exemplo](https://github.com/LEMSantos/pygutils/blob/main/pygutils/examples/animation_example.py)

```python
class pygutils.animation.Animation(
    frames_sequence: list[pygame.Surface],
    animation_speed: int,
    on_finish: Callable[[], None] | None = None,
    loop: bool = True)
```

Classe que representa uma animação a partir de uma sequência de frames que são devolvidos em uma certa velocidade baseado no deltatime do jogo. É possível criar animações que são executadas apenas uma vez ou em loop. Além disso, ainda é possível definir um callback que será chamado todas as vezes que a animação for finalizada.

<table>
    <tr>
        <td><strong>Parâmetros:</strong></td>
        <td>
            <strong>frames_sequence</strong>: sequência de superfícies que serão animadas;<br>
            <strong>animation_speed</strong>: velocidade em que a animação será executada;<br>
            <strong>on_finish</strong>: callback executado todas as vezes que a animação é concluída. Nulo por padrão;<br>
            <strong>loop</strong>: flag que identifica se a animação deve ser executada continuamente ou apenas uma vez. Verdadeira por padrão.<br>
        </td>
    </tr>
</table>

#### Métodos e propriedades

```python
property Animation.finished -> bool
```
- Propriedade que identifica se a animação foi finalizada. Em loops essa propriedade fica verdadeira apenas até a próxima chamada do método `update`.

```python
Animation.next(self) -> pygame.Surface
```
- Método que retorna a próxima superfície da sequência.

```python
Animation.reset(self) -> None
```
- Método que retorna a animação para o estado inicial.

```python
Animation.update(self, delta_time: float) -> None
```
- Método que atualiza o índice da animação, chama o callback na finalização e reseta automaticamente caso seja uma animação em loop. Esse método deve ser chamado apenas uma vez a cada frame do jogo. O <strong>delta_time</strong> representa o tempo entre dois frames consecutivos.


<div id="event" />

### Event -- [Exemplo](https://github.com/LEMSantos/pygutils/blob/main/pygutils/examples/event_example.py)

```python
class pygutils.event.EventManager()
```

Classe que implementa o padrão de projeto Observer, que consiste em um mecanismo de assinatura para notificar multiplos objetos sobre qualquer evento que aconteça no objeto que está sendo observado. Essa classe pode ser utilizada para herança, que permite a qualquer classe se tornar um `publisher`, ou como um atributo público no objeto que será observado. Qualquer classe que atuará como `subscriber` deve possuir um método com a assinatura:

```python
def notify(self, event: str, *args, **kwargs) -> None: ...
```

#### Métodos e propriedades

```python
property EventManager.listeners -> dict[str, set[EventListener]]
```
- Propriedade que retorna o mapa de cada evento e dos subscribers registrados para ele.

```python
EventManager.subscribe(self, event: str, listener: EventListener) -> None
```
- Permite que um objeto que atenda as especificações possa receber as notificações emitidas através do manager.
<table align="center">
    <tr>
        <td><strong>Parâmetros:</strong></td>
        <td>
            <strong>event</strong>: string que identifica o evento;<br>
            <strong>listener</strong>: objeto que será registrado para ser notificado quando o evento for emitido.<br>
        </td>
    </tr>
</table>

```python
EventManager.unsubscribe(self, event: str, listener: EventListener) -> None
```
- Permite que um objeto saia da lista de notificações de um evento específico.
<table align="center">
    <tr>
        <td><strong>Parâmetros:</strong></td>
        <td>
            <strong>event</strong>: string que identifica o evento;<br>
            <strong>listener</strong>: objeto que será retirado da lista de notificações para o evento.<br>
        </td>
    </tr>
</table>

```python
EventManager.notify(self, event: str, *args, **kwargs) -> None
```
- Notifica todos os objetos registrado para o evento que está sendo emitido.
<table align="center">
    <tr>
        <td><strong>Parâmetros:</strong></td>
        <td>
            <strong>event</strong>: string que identifica o evento;<br>
            <strong>*args</strong>: argumentos posicionais adicionais que serão passados na hora da notificação;<br>
            <strong>**args</strong>: argumentos nomeados adicionais que serão passados na hora da notificação.<br>
        </td>
    </tr>
</table>


<div id="timer" />

### Timer -- [Exemplo](https://github.com/LEMSantos/pygutils/blob/main/pygutils/examples/timer_example.py)

```python
class pygutils.timer.Timer(
    duration_ms: int,
    callback: Callable[[], None] | None = None)
```

Classe que implementa um mecanismo para contabilizar o tempo decorrido e executar uma ação baseada em um callback passado como parâmetro para a instância. Com essa classe é possível implementar cooldowns e ações que precisam acontecer apenas uma vez após um determinado tempo.

<table>
    <tr>
        <td><strong>Parâmetros:</strong></td>
        <td>
            <strong>duration_ms</strong>: tempo de duração do timer em milissegundos;<br>
            <strong>callback</strong>: ação que será executada após o tempo de duração ser finalizado.<br>
        </td>
    </tr>
</table>

#### Métodos e propriedades

```python
property Timer.active -> bool
```
- Propriedade que identifica se o timer está ativo, ou seja, ainda não passou o tempo necessário para atingir a duração especificada.

```python
Timer.activate(self) -> None
```
- Ativa a contagem do timer. Ele pode ser reativado quantas vezes forem necessárias.

```python
Timer.deactivate(self) -> None
```
- Desabilita a contagem do timer. Esse método é chamado automaticamente após o tempo de duração chegar ao fim.

```python
Timer.update(self) -> None
```
- Verifica se o timer já foi finalizado, executa o callback, caso seja especificado, e desativa a contagem. Esse método deve ser chamado apenas uma vez a cada frame do jogo.
