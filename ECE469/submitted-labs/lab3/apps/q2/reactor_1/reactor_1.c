//#include "lab2-api.h"
#include "usertraps.h"
#include "misc.h"
//#include "prod_cons.h"

void main(int argc, char * argv[])
{
  mbox_t h_mbox_h2o, h_mbox_h2, h_mbox_o2;
  //int counter;
  //int h2_counter,o2_counter;
  sem_t s_procs_completed; // Semaphore to signal the original process that we're done 
  char * msg = NULL;
  *(msg) = 'A'; //the dummy message
  h_mbox_h2o = dstrtol(argv[1], NULL, 10);
  h_mbox_h2 = dstrtol(argv[2],NULL, 10);
  h_mbox_o2 = dstrtol(argv[3],NULL, 10);
  //counter = dstrtol(argv[4],NULL,10);

  s_procs_completed = dstrtol(argv[4], NULL, 10);

  //receive h2o twice
  if (mbox_recv(h_mbox_h2o, sizeof(msg), (void *) msg) == MBOX_FAIL) {
    Printf("\nCould not receive message in pid = %d!\n", getpid());
    Exit();
  }
  
  if (mbox_recv(h_mbox_h2o, sizeof(msg), (void *) msg) == MBOX_FAIL) {
    Printf("\nCould not receive message in pid = %d!\n", getpid());
    Exit();
  }
  Printf("\nH2 created in reactor 1\n");
  Printf("\nH2 created in reactor 1\n");
  Printf("\nO2 created in reactor 1\n");

  //now send H2 twice and O2 once
  if (mbox_send(h_mbox_h2, sizeof(msg), (void *) msg) == MBOX_FAIL) {
    Printf("\nCould not send message to mailbox %d in (%d)\n", h_mbox_h2, getpid());
    Exit();
    }
  if (mbox_send(h_mbox_h2, sizeof(msg), (void *) msg) == MBOX_FAIL) {
    Printf("\nCould not send message to mailbox %d in (%d)\n", h_mbox_h2, getpid());
    Exit();
    }
  if (mbox_send(h_mbox_o2, sizeof(msg), (void *) msg) == MBOX_FAIL) {
    Printf("\nCould not send message to mailbox %d in (%d)\n", h_mbox_o2, getpid());
    Exit();
    }
  

  //Printf("\nreactor_1 is terminated.\nWe created %d o2, and %d h2\n", o2_counter,h2_counter);
  if(sem_signal(s_procs_completed) != SYNC_SUCCESS) {
    Printf("Bad semaphore s_procs_completed (%d) in ", s_procs_completed); Printf(argv[0]); Printf(", exiting...\n");
    Exit();
  }
}