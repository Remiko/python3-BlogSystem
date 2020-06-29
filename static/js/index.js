var gitalk = new Gitalk({
          clientID: 'e68762faa1a81afacabb',
          clientSecret: 'fbd61bd02c4b60b56805aba06d020a32e098afaa',
          repo: 'https://github.com/Remiko/gitalk-store-repo',
          owner: 'Remiko',
          admin: ['Remiko'],
          id: location.pathname,      // Ensure uniqueness and length less than 50
          distractionFreeMode: false  // Facebook-like distraction free mode
        })
        gitalk.render('gitalk-container')