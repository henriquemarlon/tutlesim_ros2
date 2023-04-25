# Turtlesim: simulando um ambiente robótico integrado no ROS

## Descrição:
Para a implementação foi necessário criar um nó que controla seu movimento. Para isso, eu precisei instalar e configurar o ROS2 no POP OS 22.04 e utilizar as bibliotecas rclpy e geometry_msgs para criar um nó chamado "turtle_controller". Este nó publica mensagens no tópico "turtle1/cmd_vel" e é definido como uma subclasse da classe "Node" da biblioteca rclpy. A função "diamond" controla a ordem e a duração dos movimentos, chamando as funções de movimento apropriadas em intervalos determinados.

A função "draw" inicia o nó do ROS e encerra o nó depois que o movimento é concluído. Quando executado, o código publica mensagens de movimento no tópico "turtle1/cmd_vel" para controlar a tartaruga e imprimir a mensagem "The turtle is moving" na tela para indicar que a tartaruga está se movendo.

Para garantir a execução bem sucedida da atividade, é necessário abrir dois terminais no POP OS. O primeiro termianl é responsável por rodar o nó do "turtlesim". No segundo terminal, o código é executado e, através do ROS2, é possível movimentar a tartaruga no turtlesim publicando informações no tópico "turtle1/cmd_vel". Vale ressaltar que estamos em um contexto de comunicação em que um publicador e um subscriber se comunicam entre si ( pub-sub ).

Por fim, a tartaruga foi programada para desenhar um losango utilizando quatro funções executadas de acordo com o um temporizador.

## Link de demo:
https://www.youtube.com/watch?v=kLFpDWysuiQ

## Estrutura do Projeto:

```
.
├── LICENSE
├── README.md
├── requirements.txt
└── turtlesim_ros2.py

```
