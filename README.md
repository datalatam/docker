# docker


Estos son los ejemplos del [Curso Profesional Data Latam Despliegue Productos de Datos con Docker](https://www.meetup.com/es-ES/DataLatam/events/253599463/).

No importa el sistema operativo que usas, siempre y cuando permita la instalación de una versión reciente de docker (Windows, OSX y Linux). Antes de comenzar con los ejemplos por favor verifica lo siguiente.

## Que tienes una versión de docker actualizada. 
Vamos a trabajar con la versión de docker Community Edition (docker CE) 18.06. Para verificar la versión que tienes instalada puedes correr en la consola:

    docker --version

La respuesta debería ser por lo menos (puede ser una versión más reciente):

    $ Docker version 18.06.1-ce, build e68fc7a

## 1. Mac 
Para instalar Docker CE en un mac puedes seguir las instrucciones que están aquí:

     https://store.docker.com/editions/community/docker-ce-desktop-mac

El proceso debe ser reconocible como has instalado otros paquetes.

## 2. Windows 10 Professional
Si tienes un computador con Windows 10 Professional puedes seguir las instrucciones aquí:

    https://store.docker.com/editions/community/docker-ce-desktop-windows

El instalador, y después la aplicación Docker Desktop hacen la verificación de la instalación fácil.

## 3. Otras Versiones de Windows
Si tienes una versión de Windows 10 diferente a Profesional (por ejemplo el Home Edition) una versión anterior de Windows, hasta donde va nuestra experiencia, el instalador arriba no va a funcionar. Intentalo primero, porque es la forma más fácil. Pero si no corre, entonces puedes descargar e instalar VirtualBox, para que puedas correr Docker en una máquina virtual sobre linux.
Primero baja una version de VirtualBox aqui, e instalalo en tu computador.

    https://www.virtualbox.org/wiki/Downloads

Después baja una imagen de ubuntu desktop:

    https://www.ubuntu.com/download/desktop

Para instalar ubuntu usando Virtual Box necesitas indicar que quieres que corra la primera vez usando la imagen que bajaste antes. Hay una video del resto del proceso aquí:

    https://www.youtube.com/watch?v=GGorVpzZQwA

(es para la Versión anterior de ubuntu, pero los pasos son prácticamente iguales).

## 4. Linux (en especial Ubuntu).

Para instalar docker en ubuntu, sigue los pasos aquí:

https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-18-04

Si nunca has trabajado con una terminal, pero te tocó instalar docker sobre Ubuntu en una máquina virtual ¡no te desesperes! Lo miramos juntos el la sesión pre-curso para ayudarte de forma remota. 

## Organiza
Este evento lo organiza [Data Latam](http://wwww.datalatam.com) en cooperación con [ixpantia](https://www.ixpantia.com). Data Latam es una comunidad Latinoamericana de profesionales y académicos aplicando ciencia de datos en su día a día en la industria de datos en Latino América. En sus eventos, cursos y programas de extensión exploramos tecnologías, aprendemos sobre ciencia de datos, hablamos de tendencias y eventos relevantes de la industria, y compartimos novedades del sector.
