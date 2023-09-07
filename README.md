# Remove BG

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
    python -m venv removebg #or any name that you want
    ```
3. Execute sending the input image and de desired output:
    ```bash
    python removebg input.jpg output.png #eg: img/portfolio-perfil.jpeg img/portfolio-perfil.png
    ```

 ### Using Docker
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
    python removebg input.jpg output.png #eg: img/portfolio-perfil.jpeg img/portfolio-perfil.png
    ```