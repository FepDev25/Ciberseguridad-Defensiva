# Términos relevantes y componentes de un criptosistema

- Criptografía: es la práctica y el estudio de técnicas que permiten garantizar la confidencialidad, integridad, autenticación y no repudio de la información que se encuentra almacenada, en tránsito y en uso

- Criptosistema: En criptografía, un criptosistema es un conjunto de elementos criptográficos necesarios para implementar un servicio de seguridad concreto, como la confidencialidad. Normalmente, un criptosistema consta de dos algoritmos, uno para el cifrado y otro para el descifrado, y dos claves, una para el cifrado y otra para el descifrado. Adicionalmente, puede contener otros elementos como un algoritmo de generación de claves para implementar determinados servicios de seguridad.

- Texto plano: son los datos brutos que deben protegerse durante la transmisión del emisor al receptor. El texto plano también suele denominarse texto en claro o mensaje. El objetivo es que al final del proceso sólo el emisor y el receptor conozcan el texto plano. Un interceptor no debe poder obtener el texto plano.

- Texto cifrado: es la versión ininteligible del texto plano que resulta de aplicar el algoritmo de cifrado y la clave de cifrado al texto plano. El texto cifrado también suele denominarse criptograma. El texto cifrado no es secreto y puede ser obtenido por cualquiera que tenga acceso al canal de comunicación.

- Cifrar: Proceso de convertir información ordinaria (texto plano) en una forma ininteligible (texto cifrado) mediante la aplicación de un algoritmo de cifrado y una clave de cifrado.

- Descifrar: Proceso de convertir texto cifrado en texto plano mediante la aplicación de un algoritmo de descifrado y una clave de descifrado.

- Algoritmo de cifrado: Algoritmo criptográfico que toma como entrada un texto plano y una clave de cifrado, y produce un texto cifrado. La elección del algoritmo de cifrado debe ser acordada entre el emisor y el receptor. Un interceptor puede o no conocer el algoritmo de cifrado utilizado.

- Algoritmo de descifrado: Algoritmo criptográfico que toma como entrada un texto cifrado y una clave de descifrado, y produce un texto plano. El algoritmo de descifrado "invierte" el algoritmo de cifrado y, por tanto, está estrechamente relacionado con él. Un interceptor puede o no conocer el algoritmo de descifrado utilizado.

- Clave de cifrado: La clave de cifrado es un valor conocido por el emisor. El emisor introduce la clave en el algoritmo de cifrado junto con el texto plano para calcular el texto cifrado. Normalmente, el receptor también conoce la clave de cifrado. Un interceptor puede conocerla o no.

- Clave de descifrado: La clave de descifrado es un valor conocido por el receptor. La clave de descifrado está relacionada con la clave de cifrado, pero no siempre es idéntica. El receptor introduce la clave de descifrado en el algoritmo de descifrado junto con el texto cifrado para calcular el texto plano. El emisor puede conocerla o no. El interceptor no debe conocer la clave de descifrado. El conjunto de todas las claves de descifrado posibles se denomina espacio de claves.

- Interceptor (también suele referirse como adversario o atacante): es una entidad distinta del emisor o el receptor que intenta determinar el texto plano. El interceptor podrá ver el texto cifrado. El interceptor puede conocer el algoritmo de cifrado y/o descifrado. La única información que el interceptor nunca debe conocer es la clave de descifrado.

Criptosistema simétrico: Se corresponde con un criptosistema en el que la clave de cifrado y la clave de descifrado son esencialmente la misma (en situaciones en las que no son exactamente iguales, son muy parecidas). El emisor y el receptor deben ser las únicas personas que conozcan esta clave. Todos los criptosistemas anteriores a los años 70 eran simétricos y siguen siendo muy populares en la actualidad. El estudio de los criptosistemas simétricos suele denominarse criptografía simétrica. Los criptosistemas simétricos también se conocen como criptosistemas de clave secreta.

Criptosistema asimétrico: Se corresponde con un criptosistema en el que la clave de cifrado y la clave de descifrado son fundamentalmente diferentes. También suelen denominarse criptosistemas de clave pública. Mientras que el receptor mantenga la clave de descifrado en secreto (algo que se debe hacer en cualquier criptosistema), no es necesario que la clave de cifrado sea secreta. En estos criptosistemas es “imposible” (computacionalmente inviable) determinar la clave de descifrado a partir de la clave de cifrado. El estudio de los criptosistemas de clave pública suele denominarse criptografía asimétrica o de clave pública.
