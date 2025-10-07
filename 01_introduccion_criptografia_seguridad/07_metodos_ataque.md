# Metodos de ataque

## Fuerza bruta

- Se basa en ciphertext-only attack.
- Consiste eb:
  - El atacante intercepta el texto cifrado con un Criptosistema conocido.
  - El atacante selecciona una clave del espacio de claves.
  - El atacante intenta descifrar el texto cifrado utilizando esa clave y comprueba si el resultado tiene sentido.
  - Si el texto plano resultante tiene sentido, entonces el atacante ha encontrado la clave de cifrado. En caso contrario, selecciona otra clave y comienza de nuevo el proceso.

### Importancia del espacio de claves

- Comprende todas las claves de descifrado posibles para un criptosistema concreto.
- Para evitar un ataque de fuerza bruta, deben existir suficientes claves de  descifrado como para que no resulte práctico el proceso. Ya sea por que consume demasiado tiempo o demasiado dinero

## Otros metodos de ataque

- Time memory trade-off attacks
- Primitive-specific attacks
- Side-channel attacks
