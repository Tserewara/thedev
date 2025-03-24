#!/bin/sh

# Initial certificate request
certbot certonly --webroot -w /var/www/certbot \
    --email your-email@example.com \
    --agree-tos \
    --no-eff-email \
    -d thedev.com.br \
    -d www.thedev.com.br \
    --rsa-key-size 4096 \
    --non-interactive \
    --force-renewal