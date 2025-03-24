FROM nginx:1.25

# Install Certbot
RUN apt-get update && \
    apt-get install -y certbot python3-certbot-nginx && \
    rm -rf /var/lib/apt/lists/*

# Copy configuration
COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY certbot-init.sh /docker-entrypoint.d/certbot-init.sh
RUN chmod +x /docker-entrypoint.d/certbot-init.sh

EXPOSE 80 443