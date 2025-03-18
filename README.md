O código utiliza a biblioteca threading para executar dois processos em paralelo. A função process(name, duration) simula um processo, exibindo uma mensagem de início, aguardando um tempo determinado (duration) e depois exibindo uma mensagem de término.

Na função main(), duas threads (thread1 e thread2) são criadas e iniciadas, rodando a função process com diferentes tempos de espera (2 e 3 segundos, respectivamente). O método .join() é utilizado para garantir que ambas as threads terminem antes de exibir a mensagem final "Both processes finished".
