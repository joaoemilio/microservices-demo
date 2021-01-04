ARG STACK_VERSION=7.10.0-SNAPSHOT
#FROM docker.elastic.co/beats/heartbeat:${STACK_VERSION}
FROM docker.elastic.co/observability-ci/heartbeat:7.10.0-synthetics
USER root
RUN yum -y install epel-release && \
    yum -y install atk cups gtk gdk xrandr pango.x86_64 libXcomposite.x86_64 libXcursor.x86_64 libXdamage.x86_64 \
	  libXext.x86_64 libXi.x86_64 libXtst.x86_64 cups-libs.x86_64 libXScrnSaver.x86_64 libXrandr.x86_64 GConf2.x86_64 \
	  alsa-lib.x86_64 atk.x86_64 gtk3.x86_64 ipa-gothic-fonts xorg-x11-fonts-100dpi xorg-x11-fonts-75dpi xorg-x11-utils \
	  xorg-x11-fonts-cyrillic xorg-x11-fonts-Type1 xorg-x11-fonts-misc \
	  yum clean all && \
    rm -rf /var/cache/yum


ENV TINI_VERSION v0.19.0
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /tini
RUN chmod +x /tini
ENTRYPOINT ["/tini", "--", "/usr/local/bin/docker-entrypoint", "-e"]

RUN echo /usr/share/heartbeat/.node \\
      /usr/share/heartbeat/.npm \\
      /usr/share/heartbeat/.cache \\
      /usr/share/heartbeat/.config \\
      /opt/elastic-synthetics | xargs -IDIR sh -c "mkdir DIR && chown -R heartbeat DIR"

ENV NODE_PATH=/usr/share/heartbeat/.node

#COPY examples/todos /opt/examples/todos
#RUN chown -R heartbeat /opt/examples
RUN chown -R heartbeat /usr/share/heartbeat
RUN chmod -R 755 heartbeat /usr/share/heartbeat

USER heartbeat
RUN  cd /usr/share/heartbeat/.node \\
      && mkdir node \\
      && curl https://nodejs.org/dist/v12.18.4/node-v12.18.4-linux-x64.tar.xz | tar -xJ --strip 1 -C node
ENV PATH="/usr/share/heartbeat/.node/node/bin:$PATH"
RUN npm i -g @elastic/synthetics@alpha
