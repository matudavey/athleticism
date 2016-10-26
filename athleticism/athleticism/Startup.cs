using Microsoft.Owin;
using Owin;

[assembly: OwinStartupAttribute(typeof(athleticism.Startup))]
namespace athleticism
{
    public partial class Startup {
        public void Configuration(IAppBuilder app) {
            ConfigureAuth(app);
        }
    }
}
