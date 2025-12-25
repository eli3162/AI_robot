sudo apt install curl git

curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
rustup toolchain install nightly
curl -LsSf https://astral.sh/uv/install.sh | sh
sudo apt install nodejs
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash

git clone https://github.com/exo-explore/exo

cd exo/dashboard && npm install && npm run build && cd ..

uv run exo
