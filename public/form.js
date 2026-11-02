async function enviarLead(e) {
        e.preventDefault();
        const form = e.target;
        const btn = document.getElementById('btn-submit');
        const sucesso = document.getElementById('sucesso-msg');
        const erro = document.getElementById('erro-msg');
        
        const scriptTag = document.currentScript || document.querySelector('script[data-endpoint]');
        const endpoint = scriptTag ? scriptTag.getAttribute('data-endpoint') : '';
        const ga4Id = scriptTag ? scriptTag.getAttribute('data-ga4') : '';

        btn.disabled = true;
        btn.textContent = 'Enviando...';
        erro.classList.add('hidden');

        const formData = new FormData(form);
        const data = Object.fromEntries(formData.entries());

        try {
            const response = await fetch(endpoint, {
                method: 'POST',
                headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' },
                body: JSON.stringify(data)
            });

            if (response.ok) {
                form.classList.add('hidden');
                sucesso.classList.remove('hidden');

                if (ga4Id && typeof gtag === 'function') {
                    gtag('event', 'generate_lead', {
                        'event_category': 'Conversao',
                        'event_label': data.cidade || 'Landing Page',
                        'tipo_plano': data.tipo_plano
                    });
                }
            } else {
                throw new Error('Falha no envio');
            }
        } catch (err) {
            console.error(err);
            erro.classList.remove('hidden');
            btn.disabled = false;
            btn.textContent = 'Solicitar cotação';
        }
    }