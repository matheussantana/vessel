#!/usr/bin/env bash

#certbot certonly   --dry-run --webroot --agree-tos --no-eff-email --email <YOUR-EMAIL> --config-dir /etc/letsencrypt --logs-dir /var/log/letsencrypt -w /var/www/letsencrypt -d <DOMAIN>

#openssl req -newkey rsa:4096             -x509             -sha256             -days 3650             -nodes             -out example.crt             -keyout example.key