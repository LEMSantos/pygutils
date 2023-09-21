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
- Event
- Timer


<div id="animation" />

### Animation -- [Exemplo](https://github.com/LEMSantos/pygutils/examples/animation_example.py)

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
