<p align="center">
    <img src="docs/logo.jpeg" width="600" alt="Remove BG">
</p>

------
Remove the backgrounf of your images JPG automatically.

## Description
`RemoveBG` is a command line tool that allows you to remove the backgrounf of your JPG file automatically.

It only supports JPG, JPEG and PNG.

## Requirements
- Python > 3.7, < 3.12
- Pip
- Docker (optional)

## Usage
### Using Command Line
1. Clone the repository:
    ```bash
    git clone https://github.com/CleytonBonamigo/removebg.git
    cd removebg
    ```
2. Create new virtual environment:
    ```bash
    #To create a new Virtual Env:
    python -m venv removebg #You can change the "removebg" name of venv to whatever you want.

    #To exit the venv
    deactivate

    #If you want to enter again into created Virtual Env
    source removebg/bin/activate #Change "removebg" for whatever name that you named your venv.
    ```
3. Execute sending the input image and de desired output:
    ```bash
    python ./src/removebg.py input.jpg #eg: img/portfolio-perfil.jpeg
    ```

 ### Using Docker
 It takes a while to remove the background, but it works 😆.

 1. Clone the repository:
    ```bash
    git clone https://github.com/CleytonBonamigo/removebg.git
    cd removebg
    ```
2. Run the docker command to set up the environment:
    ```bash
    docker compose up -d
    ```
3. Connect into container:
    ```bash
    docker exec -it removebg bash
    ```
4. Execute sending the input image and de desired output:
    ```bash
    python ./src/removebg.py input.jpg #eg: img/portfolio-perfil.jpeg
    ```