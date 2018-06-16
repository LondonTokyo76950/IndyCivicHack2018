using System;
using System.Collections.Generic;
using System.Linq;
using System.Net;
using System.Net.Http;
using System.Web.Http;

namespace IndyCivicHack2018.Controllers
{
    public class Test1Controller : ApiController
    {
        public string[] Get()
        {
            return new string[]
            {
            "Hello",
            "World"
            };
        }
    }
}
