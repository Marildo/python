const options = {
    moduleCache: {
      vue: Vue
    },
  
    async getFile(url) {
      const res = await fetch(url);
      console.log(url, res)
      if (!res.ok)
        console.error(new Error(res.statusText + ' ' + url), { res });
      return await res.text();
    },
  
    addStyle(textContent) {
      const style = Object.assign(document.createElement('style'), { textContent });
      const ref = document.head.getElementsByTagName('style')[0] || null;
      document.head.insertBefore(style, ref)
    },
  }
  
  const { loadModule } = window['vue3-sfc-loader'];