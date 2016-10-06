using System;
using Android.App;
using Android.Content;
using Android.Runtime;
using Android.Views;
using Android.Widget;
using Android.OS;
using Android.Util;
namespace Hello
{
    [Activity(Label = "Hello", MainLauncher = true, Icon = "@drawable/icon")]
    public class MainActivity : Activity
    {
        String tag = "Testing app ";
        protected override void OnCreate(Bundle bundle)
        {
            base.OnCreate(bundle);

            // Set our view from the "main" layout resource
             
            SetContentView(Resource.Layout.Main);

            // Get our button from the layout resource,
            // and attach an event to it
            Button button = FindViewById<Button>(Resource.Id.button1);

            button.Click += OnButtonClick;
            Log.Info(tag,"on_create() at "+DateTime.Now.ToString());
        }

        protected override void OnStart()
        {
            base.OnStart();
            Log.Info(tag, "on_start() at " + DateTime.Now.ToString());

        }


        protected override void OnPause()
        {
            base.OnPause();
            Log.Info(tag, "on_pause() at " + DateTime.Now.ToString());
        }

        protected override void OnResume() {
            base.OnResume();
            Log.Info(tag, "on_resume() at " + DateTime.Now.ToString());
        }

        protected override void OnStop()
        {
            base.OnStop();
            Log.Info(tag, "on_stop() at " + DateTime.Now.ToString());
        }

        protected override void OnDestroy()
        {
            base.OnDestroy();
            Log.Info(tag, "on_destroy() at " + DateTime.Now.ToString());
        }

        void OnButtonClick(object sender, EventArgs args)
        {
            LinearLayout lt  = FindViewById<LinearLayout>(Resource.Id.linearLayout2);
            lt.Visibility = ViewStates.Visible; 
        }
    }
}

