import time

import visdom
import torch

viz = visdom.Visdom()


def update_single(iteration, loss, window, update_type, epoch_size):
    viz.line(
        X=torch.ones((1, 1)).cpu() * iteration,
        Y=torch.Tensor([loss]).unsqueeze(0).cpu() / epoch_size,
        win=window,
        update=update_type
    )
    if iteration == 0:
        viz.line(
            X=torch.zeros((1, 1)).cpu(),
            Y=torch.Tensor([loss]).unsqueeze(0).cpu(),
            win=window, update=True
        )


def update_vis_plot(iteration, loc, conf, window1, window2, update_type,
                    epoch_size=1):
    viz.line(
        X=torch.ones((1, 3)).cpu() * iteration,
        Y=torch.Tensor([loc, conf, loc + conf]).unsqueeze(0).cpu() / epoch_size,
        win=window1,
        update=update_type
    )
    # initialize epoch plot on first iteration
    if iteration == 0:
        viz.line(
            X=torch.zeros((1, 3)).cpu(),
            Y=torch.Tensor([loc, conf, loc + conf]).unsqueeze(0).cpu(),
            win=window2,
            update=True
        )


def create_vis_plot(_xlabel, _ylabel, _title, _legend):
    return viz.line(
        X=torch.zeros((1,)).cpu(),
        Y=torch.zeros((1, 3)).cpu(),
        opts=dict(
            xlabel=_xlabel,
            ylabel=_ylabel,
            title=_title,
            legend=_legend
        )
    )


vis_title = 'SRGAN vis'
vis_legend = ['Loc Loss', 'Conf Loss', 'Total Loss']
iter_plot = create_vis_plot('Iteration', 'Loss', vis_title, vis_legend)
# epoch_plot = create_vis_plot('Epoch', 'Loss', vis_title, vis_legend)

for epoch in range(100):
    update_single(epoch, 0.01 * epoch, iter_plot, 'append', 100)
    # update_vis_plot(epoch, 0.01 * epoch, 0.02 * epoch, iter_plot, epoch_plot, 'append', 100)
    # time.sleep(3)
